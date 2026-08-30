local function reply(cb, payload)
    cb(payload or { ok = true })
end

-- Prefer the current REGISTER_NUI_CALLBACK native per current FiveM documentation.
RegisterNuiCallback('example:ping', function(data, cb)
    if type(data) ~= 'table' then
        reply(cb, { ok = false, error = { code = 'invalid_payload', message = 'Invalid payload' } })
        return
    end

    reply(cb, { ok = true, data = { pong = true } })
end)
