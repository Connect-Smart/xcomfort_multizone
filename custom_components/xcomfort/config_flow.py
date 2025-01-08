###Version 1.3.5
from homeassistant.const import CONF_NAME
import voluptuous as vol
import logging
from homeassistant import config_entries

class xComfortConfigFlow(config_entries.ConfigFlow, domain='xcomfort'):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="xComfort", data=user_input)

        zones = await self.api.get_zones()
        schema = vol.Schema({vol.Required("zone", default=zones[0]): vol.In(zones)})
        return self.async_show_form(step_id="user", data_schema=schema)
