local RESOURCE = GetCurrentResourceName()

AddEventHandler('onResourceStop', function(resourceName)
    if resourceName ~= RESOURCE then return end
    -- Release focus, cameras, entities, handlers, and other owned client state here.
end)
