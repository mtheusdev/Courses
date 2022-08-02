const port = 3003

const express = require('express')
const server = express()
const allowCors = require('./cors')

server.use(express.json())
server.use(allowCors)
server.use(express.urlencoded({ extended: true}))

server.listen(port, () => {
  console.log('Server running on port 3003')
})

module.exports = server