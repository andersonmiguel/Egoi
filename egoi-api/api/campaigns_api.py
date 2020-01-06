# coding: utf-8

"""
    APIv3 (Beta)

     # Introduction Just a quick pick!!! This is our new version of API. Remember, it is not stable yet!!! But we invite you play with it and give us your feedback ;) # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # HTTP Methods for RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0-beta
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from egoi-api.api_client import ApiClient
from egoi-api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class CampaignsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_campaigns(self, campaign_hash, **kwargs):  # noqa: E501
        """Remove Campaign  # noqa: E501

        Remove campaign information given its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_campaigns(campaign_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str campaign_hash: ID of the Campaign (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_campaigns_with_http_info(campaign_hash, **kwargs)  # noqa: E501

    def delete_campaigns_with_http_info(self, campaign_hash, **kwargs):  # noqa: E501
        """Remove Campaign  # noqa: E501

        Remove campaign information given its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_campaigns_with_http_info(campaign_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str campaign_hash: ID of the Campaign (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['campaign_hash']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_campaigns" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'campaign_hash' is set
        if self.api_client.client_side_validation and ('campaign_hash' not in local_var_params or  # noqa: E501
                                                        local_var_params['campaign_hash'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `campaign_hash` when calling `delete_campaigns`")  # noqa: E501

        if self.api_client.client_side_validation and 'campaign_hash' in local_var_params and not re.search(r'[a-zA-Z0-9_-]*', local_var_params['campaign_hash']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `campaign_hash` when calling `delete_campaigns`, must conform to the pattern `/[a-zA-Z0-9_-]*/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'campaign_hash' in local_var_params:
            path_params['campaign_hash'] = local_var_params['campaign_hash']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/campaigns/{campaign_hash}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_campaigns(self, **kwargs):  # noqa: E501
        """Get all Campaigns  # noqa: E501

        Returns all campaigns  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_campaigns(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str channel: Channel of the campaign
        :param str campaign_hash: Hash of the campaign
        :param int list_id: ID of the list where the campaign belongs
        :param str status: Status of the campaign
        :param str internal_name: Internal name of the campaign
        :param int created_by: ID of the user who created the campaign
        :param int group_id: ID of the group where the campaign belongs
        :param datetime created_min: Created initial date
        :param datetime created_max: Created finish
        :param datetime updated_min: Updated initial
        :param datetime updated_max: Updated finish
        :param date start_date_min: Start date initial
        :param date start_date_max: Start date finish
        :param date end_date_min: End Date initial
        :param date end_date_max: End Date finish
        :param date schedule_date_min: Schedule Date initial
        :param date schedule_date_max: Schedule Date finish
        :param int offset: Element offset (starting at zero for the first element)
        :param int limit: Number of items to return
        :param str order: Type of order
        :param str order_by: Reference attribute to order campaigns
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CampaignsCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_all_campaigns_with_http_info(**kwargs)  # noqa: E501

    def get_all_campaigns_with_http_info(self, **kwargs):  # noqa: E501
        """Get all Campaigns  # noqa: E501

        Returns all campaigns  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_campaigns_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str channel: Channel of the campaign
        :param str campaign_hash: Hash of the campaign
        :param int list_id: ID of the list where the campaign belongs
        :param str status: Status of the campaign
        :param str internal_name: Internal name of the campaign
        :param int created_by: ID of the user who created the campaign
        :param int group_id: ID of the group where the campaign belongs
        :param datetime created_min: Created initial date
        :param datetime created_max: Created finish
        :param datetime updated_min: Updated initial
        :param datetime updated_max: Updated finish
        :param date start_date_min: Start date initial
        :param date start_date_max: Start date finish
        :param date end_date_min: End Date initial
        :param date end_date_max: End Date finish
        :param date schedule_date_min: Schedule Date initial
        :param date schedule_date_max: Schedule Date finish
        :param int offset: Element offset (starting at zero for the first element)
        :param int limit: Number of items to return
        :param str order: Type of order
        :param str order_by: Reference attribute to order campaigns
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CampaignsCollection, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['channel', 'campaign_hash', 'list_id', 'status', 'internal_name', 'created_by', 'group_id', 'created_min', 'created_max', 'updated_min', 'updated_max', 'start_date_min', 'start_date_max', 'end_date_min', 'end_date_max', 'schedule_date_min', 'schedule_date_max', 'offset', 'limit', 'order', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_campaigns" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_all_campaigns`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_all_campaigns`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_all_campaigns`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel' in local_var_params and local_var_params['channel'] is not None:  # noqa: E501
            query_params.append(('channel', local_var_params['channel']))  # noqa: E501
        if 'campaign_hash' in local_var_params and local_var_params['campaign_hash'] is not None:  # noqa: E501
            query_params.append(('campaign_hash', local_var_params['campaign_hash']))  # noqa: E501
        if 'list_id' in local_var_params and local_var_params['list_id'] is not None:  # noqa: E501
            query_params.append(('list_id', local_var_params['list_id']))  # noqa: E501
        if 'status' in local_var_params and local_var_params['status'] is not None:  # noqa: E501
            query_params.append(('status', local_var_params['status']))  # noqa: E501
        if 'internal_name' in local_var_params and local_var_params['internal_name'] is not None:  # noqa: E501
            query_params.append(('internal_name', local_var_params['internal_name']))  # noqa: E501
        if 'created_by' in local_var_params and local_var_params['created_by'] is not None:  # noqa: E501
            query_params.append(('created_by', local_var_params['created_by']))  # noqa: E501
        if 'group_id' in local_var_params and local_var_params['group_id'] is not None:  # noqa: E501
            query_params.append(('group_id', local_var_params['group_id']))  # noqa: E501
        if 'created_min' in local_var_params and local_var_params['created_min'] is not None:  # noqa: E501
            query_params.append(('created_min', local_var_params['created_min']))  # noqa: E501
        if 'created_max' in local_var_params and local_var_params['created_max'] is not None:  # noqa: E501
            query_params.append(('created_max', local_var_params['created_max']))  # noqa: E501
        if 'updated_min' in local_var_params and local_var_params['updated_min'] is not None:  # noqa: E501
            query_params.append(('updated_min', local_var_params['updated_min']))  # noqa: E501
        if 'updated_max' in local_var_params and local_var_params['updated_max'] is not None:  # noqa: E501
            query_params.append(('updated_max', local_var_params['updated_max']))  # noqa: E501
        if 'start_date_min' in local_var_params and local_var_params['start_date_min'] is not None:  # noqa: E501
            query_params.append(('start_date_min', local_var_params['start_date_min']))  # noqa: E501
        if 'start_date_max' in local_var_params and local_var_params['start_date_max'] is not None:  # noqa: E501
            query_params.append(('start_date_max', local_var_params['start_date_max']))  # noqa: E501
        if 'end_date_min' in local_var_params and local_var_params['end_date_min'] is not None:  # noqa: E501
            query_params.append(('end_date_min', local_var_params['end_date_min']))  # noqa: E501
        if 'end_date_max' in local_var_params and local_var_params['end_date_max'] is not None:  # noqa: E501
            query_params.append(('end_date_max', local_var_params['end_date_max']))  # noqa: E501
        if 'schedule_date_min' in local_var_params and local_var_params['schedule_date_min'] is not None:  # noqa: E501
            query_params.append(('schedule_date_min', local_var_params['schedule_date_min']))  # noqa: E501
        if 'schedule_date_max' in local_var_params and local_var_params['schedule_date_max'] is not None:  # noqa: E501
            query_params.append(('schedule_date_max', local_var_params['schedule_date_max']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'order' in local_var_params and local_var_params['order'] is not None:  # noqa: E501
            query_params.append(('order', local_var_params['order']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('order_by', local_var_params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/campaigns', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CampaignsCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)