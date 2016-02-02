#!/usr/bin/env python
from __future__ import absolute_import

import logging
from libsaml.backend import SAML2Backend

LOG = logging.getLogger(__name__)

class CustomSAML2Backend(SAML2Backend):
  """
  Wrapper around libsaml.SAML2Backend to alter SAML username
  """

  def clean_user_main_attribute(self, main_attribute):
    """
    Maps username received by SAML to another username
    """
    LOG.warn("Using CustomSAML2Backend")
    username, extra = main_attribute.split('@')
    LOG.warn("Mapping username from %s to %s" % (main_attribute, username))
    return username

  def _set_attribute(self, obj, attr, value):
    """
    Override DjangoSaml2._set_attribute to not revert username to
    before clean_user_main_attribute
    """
    field = obj._meta.get_field_by_name(attr)
    if len(value) > field[0].max_length:
      cleaned_value = value[:field[0].max_length]
      LOG.warn('The attribute "%s" was trimmed from "%s" to "%s"' %
                  (attr, value, cleaned_value))
    else:
      cleaned_value = value

    old_value = getattr(obj, attr)

    if attr != "username":
      LOG.warn("Not reverting username to old value")
      if cleaned_value != old_value:
        setattr(obj, attr, cleaned_value)
        return True

    return False
