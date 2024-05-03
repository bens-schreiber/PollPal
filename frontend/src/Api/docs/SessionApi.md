# PollPalApi.SessionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sessionCreate**](SessionApi.md#sessionCreate) | **POST** /api/session/ | 
[**sessionDestroy**](SessionApi.md#sessionDestroy) | **DELETE** /api/session/{id} | 
[**sessionEndDestroy**](SessionApi.md#sessionEndDestroy) | **DELETE** /api/session/{session_id}/end | 
[**sessionList**](SessionApi.md#sessionList) | **GET** /api/session/ | 
[**sessionStartCreate**](SessionApi.md#sessionStartCreate) | **POST** /api/session/start | 

<a name="sessionCreate"></a>
# **sessionCreate**
> Session sessionCreate(body)



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

apiInstance.sessionCreate(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Session**](Session.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="sessionDestroy"></a>
# **sessionDestroy**
> sessionDestroy(id)



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
let id = 56; // Number | 

apiInstance.sessionDestroy(id).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="sessionEndDestroy"></a>
# **sessionEndDestroy**
> sessionEndDestroy(session_id)



Deletes a Poll from a session. If there is no Poll, return 400. If the poll is accepting answers, return 400.

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
let session_id = 56; // Number | 

apiInstance.sessionEndDestroy(session_id).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Number**|  | 

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
apiInstance.sessionList().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
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

<a name="sessionStartCreate"></a>
# **sessionStartCreate**
> Poll sessionStartCreate(body)



Creates a poll for the session with the provided question and answer.

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
let body = new PollPalApi.SessionStart(); // SessionStart | 

apiInstance.sessionStartCreate(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionStart**](SessionStart.md)|  | 

### Return type

[**Poll**](Poll.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

