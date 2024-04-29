# PollPalApi.SessionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sessionCreate**](SessionApi.md#sessionCreate) | **POST** /api/session/ | 
[**sessionDestroy**](SessionApi.md#sessionDestroy) | **DELETE** /api/session/{session_id} | 
[**sessionList**](SessionApi.md#sessionList) | **GET** /api/session/ | 

<a name="sessionCreate"></a>
# **sessionCreate**
> Session sessionCreate(body, id, label, id, label)



### Example
```javascript
import {PollPalApi} from 'poll_pal_api';
let defaultClient = PollPalApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new PollPalApi.SessionApi();
let body = new PollPalApi.Session(); // Session | 
let id = 56; // Number | 
let label = "label_example"; // String | 
let id = 56; // Number | 
let label = "label_example"; // String | 

apiInstance.sessionCreate(body, id, label, id, label, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Session**](Session.md)|  | 
 **id** | **Number**|  | 
 **label** | **String**|  | 
 **id** | **Number**|  | 
 **label** | **String**|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

<a name="sessionDestroy"></a>
# **sessionDestroy**
> sessionDestroy(sessionId)



### Example
```javascript
import {PollPalApi} from 'poll_pal_api';
let defaultClient = PollPalApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new PollPalApi.SessionApi();
let sessionId = 56; // Number | 

apiInstance.sessionDestroy(sessionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sessionId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="sessionList"></a>
# **sessionList**
> [Session] sessionList()



### Example
```javascript
import {PollPalApi} from 'poll_pal_api';
let defaultClient = PollPalApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new PollPalApi.SessionApi();
apiInstance.sessionList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Session]**](Session.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

