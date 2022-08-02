
# Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD
import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

app = Flask(__name__)


app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.jinja_env.filters["usd"] = usd


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///finance.db")


if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    rows = db.execute("SELECT * FROM stocks WHERE user_id = :user",
                          user=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']

    total = cash
    stocks = []
    for index, row in enumerate(rows):
        stock_info = lookup(row['symbol'])

        stocks.append(list((stock_info['symbol'], stock_info['name'], row['amount'], stock_info['price'], round(stock_info['price'] * row['amount'], 2))))
        total += stocks[index][4]

    return render_template("index.html", stocks=stocks, cash=round(cash, 2), total=round(total, 2))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        amount=int(request.form.get("amount"))
        symbol=lookup(request.form.get("symbol"))['symbol']

        if not lookup(symbol):
            return apology("Could not find the stock")

        price=lookup(symbol)['price']
        cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']
        cash_after = cash - price * float(amount)

        if cash_after < 0:
            return apology("You don't have enough money for this transaction")

        stock = db.execute("SELECT amount FROM stocks WHERE user_id = :user AND symbol = :symbol",
                          user=session["user_id"], symbol=symbol)

        if not stock:
            db.execute("INSERT INTO stocks(user_id, symbol, amount) VALUES (:user, :symbol, :amount)",
                user=session["user_id"], symbol=symbol, amount=amount)

        else:
            amount += stock[0]['amount']

            db.execute("UPDATE stocks SET amount = :amount WHERE user_id = :user AND symbol = :symbol",
                user=session["user_id"], symbol=symbol, amount=amount)

        db.execute("UPDATE users SET cash = :cash WHERE id = :user",
                          cash=cash_after, user=session["user_id"])

        db.execute("INSERT INTO transactions(user_id, symbol, amount, value) VALUES (:user, :symbol, :amount, :value)",
                user=session["user_id"], symbol=symbol, amount=amount, value=round(price*float(amount)))

        flash("Bought!")
        return redirect("/")

    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    rows = db.execute("SELECT * FROM transactions WHERE user_id = :user",
                            user=session["user_id"])

    transactions = []
    for row in rows:
        stock_info = lookup(row['symbol'])

        transactions.append(list((stock_info['symbol'], stock_info['name'], row['amount'], row['value'], row['date'])))

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    session.clear()
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    session.clear()

    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":

        stock = lookup(request.form.get("symbol"))

        if not stock:
            return apology("Could not find the stock")

        return render_template("quote.html", stock=stock)

    else:
        return render_template("quote.html", stock="")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    session.clear()

    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        elif request.form.get("password") != request.form.get("confirm-password"):
            return apology("The passwords don't match", 403)

        elif db.execute("SELECT * FROM users WHERE username = :username",
            username=request.form.get("username")):
            return apology("Username already taken", 403)

        db.execute("INSERT INTO users(username, hash) VALUES (:username, :hash)",
            username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))

        rows = db.execute("SELECT * FROM users WHERE username = :username",
            username=request.form.get("username"))

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":

        amount=int(request.form.get("amount"))
        symbol=request.form.get("symbol")
        price=lookup(symbol)["price"]
        value=round(price*float(amount))

        amount_before = db.execute("SELECT amount FROM stocks WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"])[0]['amount']
        amount_after = amount_before - amount

        if amount_after == 0:
            db.execute("DELETE FROM stocks WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"])

        elif amount_after < 0:
            return apology("That's more than the stocks you own")

        else:
            db.execute("UPDATE stocks SET amount = :amount WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"], amount=amount_after)

        cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']
        cash_after = cash + price * float(amount)

        db.execute("UPDATE users SET cash = :cash WHERE id = :user",
                          cash=cash_after, user=session["user_id"])

        db.execute("INSERT INTO transactions(user_id, symbol, amount, value) VALUES (:user, :symbol, :amount, :value)",
                user=session["user_id"], symbol=symbol, amount=-amount, value=value)

        flash("Sold!")
        return redirect("/")

    else:

        rows = db.execute("SELECT symbol, amount FROM stocks WHERE user_id = :user",
                            user=session["user_id"])

        stocks = {}
        for row in rows:
            stocks[row['symbol']] = row['amount']

        return render_template("sell.html", stocks=stocks)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
