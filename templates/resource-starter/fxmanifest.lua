fx_version 'cerulean'
game 'gta5'

author 'YOUR_NAME'
description 'FiveM resource'
version '0.1.0'

shared_scripts {
    'config/shared.lua',
    'shared/**/*.lua'
}

client_scripts {
    'client/**/*.lua'
}

server_scripts {
    'config/server.lua',
    'server/**/*.lua'
}
