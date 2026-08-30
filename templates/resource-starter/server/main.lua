local RESOURCE = GetCurrentResourceName()

AddEventHandler('onResourceStop', function(resourceName)
    if resourceName ~= RESOURCE then return end
    -- Idempotent server cleanup here.
end)
