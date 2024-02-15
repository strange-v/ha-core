"""The RFM Gateway component."""
# Registering devices https://developers.home-assistant.io/docs/device_registry_index/

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN

PLATFORMS = [
    Platform.BINARY_SENSOR,
    Platform.SENSOR,
]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up platform from a ConfigEntry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Forward the setup to the sensor platform.
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


# async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
#     """Set up the custom component from yaml configuration."""
#     hass.data.setdefault(DOMAIN, {})
#     return True
