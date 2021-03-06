# coding: utf-8

"""
    APIv3 (Beta)

     # Introduction Just a quick peek!!! This is our new version of API. Remember, it is not stable yet!!! But we invite you play with it and give us your feedback ;) # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  # SDK Get started quickly with E-goi with our integration tools. Our SDK is a modern open source library that makes it easy to integrate your application with E-goi services. * <b><a href='https://github.com/E-goi/sdk-java'>Java</a></b> * <b><a href='https://github.com/E-goi/sdk-php'>PHP</a></b> * <b><a href='https://github.com/E-goi/sdk-python'>Python</a></b>  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0-beta
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from egoi-api.configuration import Configuration


class HeaderFooterFooterLinks(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'forward': 'bool',
        'view_web': 'bool',
        'unsubscribe': 'bool',
        'footer_links': 'bool',
        'social_share': 'bool',
        'facebook_share': 'bool',
        'twitter_share': 'bool'
    }

    attribute_map = {
        'forward': 'forward',
        'view_web': 'view_web',
        'unsubscribe': 'unsubscribe',
        'footer_links': 'footer_links',
        'social_share': 'social_share',
        'facebook_share': 'facebook_share',
        'twitter_share': 'twitter_share'
    }

    def __init__(self, forward=False, view_web=False, unsubscribe=False, footer_links=False, social_share=False, facebook_share=False, twitter_share=False, local_vars_configuration=None):  # noqa: E501
        """HeaderFooterFooterLinks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._forward = None
        self._view_web = None
        self._unsubscribe = None
        self._footer_links = None
        self._social_share = None
        self._facebook_share = None
        self._twitter_share = None
        self.discriminator = None

        if forward is not None:
            self.forward = forward
        if view_web is not None:
            self.view_web = view_web
        if unsubscribe is not None:
            self.unsubscribe = unsubscribe
        if footer_links is not None:
            self.footer_links = footer_links
        if social_share is not None:
            self.social_share = social_share
        if facebook_share is not None:
            self.facebook_share = facebook_share
        if twitter_share is not None:
            self.twitter_share = twitter_share

    @property
    def forward(self):
        """Gets the forward of this HeaderFooterFooterLinks.  # noqa: E501

        Use view forward footer link  # noqa: E501

        :return: The forward of this HeaderFooterFooterLinks.  # noqa: E501
        :rtype: bool
        """
        return self._forward

    @forward.setter
    def forward(self, forward):
        """Sets the forward of this HeaderFooterFooterLinks.

        Use view forward footer link  # noqa: E501

        :param forward: The forward of this HeaderFooterFooterLinks.  # noqa: E501
        :type: bool
        """

        self._forward = forward

    @property
    def view_web(self):
        """Gets the view_web of this HeaderFooterFooterLinks.  # noqa: E501

        Use view view in web footer link  # noqa: E501

        :return: The view_web of this HeaderFooterFooterLinks.  # noqa: E501
        :rtype: bool
        """
        return self._view_web

    @view_web.setter
    def view_web(self, view_web):
        """Sets the view_web of this HeaderFooterFooterLinks.

        Use view view in web footer link  # noqa: E501

        :param view_web: The view_web of this HeaderFooterFooterLinks.  # noqa: E501
        :type: bool
        """

        self._view_web = view_web

    @property
    def unsubscribe(self):
        """Gets the unsubscribe of this HeaderFooterFooterLinks.  # noqa: E501

        Use view unsubscribe footer link  # noqa: E501

        :return: The unsubscribe of this HeaderFooterFooterLinks.  # noqa: E501
        :rtype: bool
        """
        return self._unsubscribe

    @unsubscribe.setter
    def unsubscribe(self, unsubscribe):
        """Sets the unsubscribe of this HeaderFooterFooterLinks.

        Use view unsubscribe footer link  # noqa: E501

        :param unsubscribe: The unsubscribe of this HeaderFooterFooterLinks.  # noqa: E501
        :type: bool
        """

        self._unsubscribe = unsubscribe

    @property
    def footer_links(self):
        """Gets the footer_links of this HeaderFooterFooterLinks.  # noqa: E501

        Use view edit footer link  # noqa: E501

        :return: The footer_links of this HeaderFooterFooterLinks.  # noqa: E501
        :rtype: bool
        """
        return self._footer_links

    @footer_links.setter
    def footer_links(self, footer_links):
        """Sets the footer_links of this HeaderFooterFooterLinks.

        Use view edit footer link  # noqa: E501

        :param footer_links: The footer_links of this HeaderFooterFooterLinks.  # noqa: E501
        :type: bool
        """

        self._footer_links = footer_links

    @property
    def social_share(self):
        """Gets the social_share of this HeaderFooterFooterLinks.  # noqa: E501

        Use view social share footer link  # noqa: E501

        :return: The social_share of this HeaderFooterFooterLinks.  # noqa: E501
        :rtype: bool
        """
        return self._social_share

    @social_share.setter
    def social_share(self, social_share):
        """Sets the social_share of this HeaderFooterFooterLinks.

        Use view social share footer link  # noqa: E501

        :param social_share: The social_share of this HeaderFooterFooterLinks.  # noqa: E501
        :type: bool
        """

        self._social_share = social_share

    @property
    def facebook_share(self):
        """Gets the facebook_share of this HeaderFooterFooterLinks.  # noqa: E501

        Use view facebook share footer link  # noqa: E501

        :return: The facebook_share of this HeaderFooterFooterLinks.  # noqa: E501
        :rtype: bool
        """
        return self._facebook_share

    @facebook_share.setter
    def facebook_share(self, facebook_share):
        """Sets the facebook_share of this HeaderFooterFooterLinks.

        Use view facebook share footer link  # noqa: E501

        :param facebook_share: The facebook_share of this HeaderFooterFooterLinks.  # noqa: E501
        :type: bool
        """

        self._facebook_share = facebook_share

    @property
    def twitter_share(self):
        """Gets the twitter_share of this HeaderFooterFooterLinks.  # noqa: E501

        Use view twitter share footer link  # noqa: E501

        :return: The twitter_share of this HeaderFooterFooterLinks.  # noqa: E501
        :rtype: bool
        """
        return self._twitter_share

    @twitter_share.setter
    def twitter_share(self, twitter_share):
        """Sets the twitter_share of this HeaderFooterFooterLinks.

        Use view twitter share footer link  # noqa: E501

        :param twitter_share: The twitter_share of this HeaderFooterFooterLinks.  # noqa: E501
        :type: bool
        """

        self._twitter_share = twitter_share

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HeaderFooterFooterLinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HeaderFooterFooterLinks):
            return True

        return self.to_dict() != other.to_dict()
