const {ipcMain} = require('electron')

ipcMain.on('blabla', (event, paths) => {
    console.log(paths)
    event.reply('process-subtitles', [
        {name:'you', amount: 900},
        {name:'he', amount: 853},
        {name:'i', amount: 1200},
        {name:'a', amount: 1200},
        {name:'she', amount: 1500},
    ])
})