# coding: utf-8

"""
    OPIF Service Data API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ClosedCaptionsUpdate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_token': 'str',
        'contact_entity_id': 'str',
        'contact_source_service_code': 'str',
        'contact_name': 'str',
        'contact_type': 'str',
        'contact_address1': 'str',
        'contact_address2': 'str',
        'contact_city': 'str',
        'contact_zip': 'str',
        'contact_zip_ext': 'str',
        'contact_state': 'str',
        'contact_phone': 'str',
        'contact_phone_ext': 'str',
        'contact_fax': 'str',
        'contact_website': 'str',
        'contact_email': 'str'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'contact_entity_id': 'contactEntityId',
        'contact_source_service_code': 'contactSourceServiceCode',
        'contact_name': 'contactName',
        'contact_type': 'contactType',
        'contact_address1': 'contactAddress1',
        'contact_address2': 'contactAddress2',
        'contact_city': 'contactCity',
        'contact_zip': 'contactZip',
        'contact_zip_ext': 'contactZipExt',
        'contact_state': 'contactState',
        'contact_phone': 'contactPhone',
        'contact_phone_ext': 'contactPhoneExt',
        'contact_fax': 'contactFax',
        'contact_website': 'contactWebsite',
        'contact_email': 'contactEmail'
    }

    def __init__(self, access_token=None, contact_entity_id=None, contact_source_service_code=None, contact_name=None, contact_type=None, contact_address1=None, contact_address2=None, contact_city=None, contact_zip=None, contact_zip_ext=None, contact_state=None, contact_phone=None, contact_phone_ext=None, contact_fax=None, contact_website=None, contact_email=None):  # noqa: E501
        """ClosedCaptionsUpdate - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._contact_entity_id = None
        self._contact_source_service_code = None
        self._contact_name = None
        self._contact_type = None
        self._contact_address1 = None
        self._contact_address2 = None
        self._contact_city = None
        self._contact_zip = None
        self._contact_zip_ext = None
        self._contact_state = None
        self._contact_phone = None
        self._contact_phone_ext = None
        self._contact_fax = None
        self._contact_website = None
        self._contact_email = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if contact_entity_id is not None:
            self.contact_entity_id = contact_entity_id
        if contact_source_service_code is not None:
            self.contact_source_service_code = contact_source_service_code
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_type is not None:
            self.contact_type = contact_type
        if contact_address1 is not None:
            self.contact_address1 = contact_address1
        if contact_address2 is not None:
            self.contact_address2 = contact_address2
        if contact_city is not None:
            self.contact_city = contact_city
        if contact_zip is not None:
            self.contact_zip = contact_zip
        if contact_zip_ext is not None:
            self.contact_zip_ext = contact_zip_ext
        if contact_state is not None:
            self.contact_state = contact_state
        if contact_phone is not None:
            self.contact_phone = contact_phone
        if contact_phone_ext is not None:
            self.contact_phone_ext = contact_phone_ext
        if contact_fax is not None:
            self.contact_fax = contact_fax
        if contact_website is not None:
            self.contact_website = contact_website
        if contact_email is not None:
            self.contact_email = contact_email

    @property
    def access_token(self):
        """Gets the access_token of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The access_token of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this ClosedCaptionsUpdate.


        :param access_token: The access_token of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def contact_entity_id(self):
        """Gets the contact_entity_id of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_entity_id of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_entity_id

    @contact_entity_id.setter
    def contact_entity_id(self, contact_entity_id):
        """Sets the contact_entity_id of this ClosedCaptionsUpdate.


        :param contact_entity_id: The contact_entity_id of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_entity_id = contact_entity_id

    @property
    def contact_source_service_code(self):
        """Gets the contact_source_service_code of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_source_service_code of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_source_service_code

    @contact_source_service_code.setter
    def contact_source_service_code(self, contact_source_service_code):
        """Sets the contact_source_service_code of this ClosedCaptionsUpdate.


        :param contact_source_service_code: The contact_source_service_code of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """
        allowed_values = ["TV"]  # noqa: E501
        if contact_source_service_code not in allowed_values:
            raise ValueError(
                "Invalid value for `contact_source_service_code` ({0}), must be one of {1}"  # noqa: E501
                .format(contact_source_service_code, allowed_values)
            )

        self._contact_source_service_code = contact_source_service_code

    @property
    def contact_name(self):
        """Gets the contact_name of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_name of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this ClosedCaptionsUpdate.


        :param contact_name: The contact_name of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def contact_type(self):
        """Gets the contact_type of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_type of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_type

    @contact_type.setter
    def contact_type(self, contact_type):
        """Sets the contact_type of this ClosedCaptionsUpdate.


        :param contact_type: The contact_type of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """
        allowed_values = ["CC"]  # noqa: E501
        if contact_type not in allowed_values:
            raise ValueError(
                "Invalid value for `contact_type` ({0}), must be one of {1}"  # noqa: E501
                .format(contact_type, allowed_values)
            )

        self._contact_type = contact_type

    @property
    def contact_address1(self):
        """Gets the contact_address1 of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_address1 of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_address1

    @contact_address1.setter
    def contact_address1(self, contact_address1):
        """Sets the contact_address1 of this ClosedCaptionsUpdate.


        :param contact_address1: The contact_address1 of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_address1 = contact_address1

    @property
    def contact_address2(self):
        """Gets the contact_address2 of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_address2 of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_address2

    @contact_address2.setter
    def contact_address2(self, contact_address2):
        """Sets the contact_address2 of this ClosedCaptionsUpdate.


        :param contact_address2: The contact_address2 of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_address2 = contact_address2

    @property
    def contact_city(self):
        """Gets the contact_city of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_city of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_city

    @contact_city.setter
    def contact_city(self, contact_city):
        """Sets the contact_city of this ClosedCaptionsUpdate.


        :param contact_city: The contact_city of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_city = contact_city

    @property
    def contact_zip(self):
        """Gets the contact_zip of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_zip of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_zip

    @contact_zip.setter
    def contact_zip(self, contact_zip):
        """Sets the contact_zip of this ClosedCaptionsUpdate.


        :param contact_zip: The contact_zip of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_zip = contact_zip

    @property
    def contact_zip_ext(self):
        """Gets the contact_zip_ext of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_zip_ext of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_zip_ext

    @contact_zip_ext.setter
    def contact_zip_ext(self, contact_zip_ext):
        """Sets the contact_zip_ext of this ClosedCaptionsUpdate.


        :param contact_zip_ext: The contact_zip_ext of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_zip_ext = contact_zip_ext

    @property
    def contact_state(self):
        """Gets the contact_state of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_state of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_state

    @contact_state.setter
    def contact_state(self, contact_state):
        """Sets the contact_state of this ClosedCaptionsUpdate.


        :param contact_state: The contact_state of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_state = contact_state

    @property
    def contact_phone(self):
        """Gets the contact_phone of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_phone of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this ClosedCaptionsUpdate.


        :param contact_phone: The contact_phone of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_phone = contact_phone

    @property
    def contact_phone_ext(self):
        """Gets the contact_phone_ext of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_phone_ext of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone_ext

    @contact_phone_ext.setter
    def contact_phone_ext(self, contact_phone_ext):
        """Sets the contact_phone_ext of this ClosedCaptionsUpdate.


        :param contact_phone_ext: The contact_phone_ext of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_phone_ext = contact_phone_ext

    @property
    def contact_fax(self):
        """Gets the contact_fax of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_fax of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_fax

    @contact_fax.setter
    def contact_fax(self, contact_fax):
        """Sets the contact_fax of this ClosedCaptionsUpdate.


        :param contact_fax: The contact_fax of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_fax = contact_fax

    @property
    def contact_website(self):
        """Gets the contact_website of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_website of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_website

    @contact_website.setter
    def contact_website(self, contact_website):
        """Sets the contact_website of this ClosedCaptionsUpdate.


        :param contact_website: The contact_website of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_website = contact_website

    @property
    def contact_email(self):
        """Gets the contact_email of this ClosedCaptionsUpdate.  # noqa: E501


        :return: The contact_email of this ClosedCaptionsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this ClosedCaptionsUpdate.


        :param contact_email: The contact_email of this ClosedCaptionsUpdate.  # noqa: E501
        :type: str
        """

        self._contact_email = contact_email

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ClosedCaptionsUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClosedCaptionsUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other