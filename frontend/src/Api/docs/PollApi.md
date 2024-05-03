# PollPalApi.PollApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pollAnswerRetrieve**](PollApi.md#pollAnswerRetrieve) | **GET** /api/poll/{poll_id}/answer | 
[**pollNextQuestionCreate**](PollApi.md#pollNextQuestionCreate) | **POST** /api/poll/next-question | 
[**pollResponsesList**](PollApi.md#pollResponsesList) | **GET** /api/poll/responses/{poll_id} | 
[**pollRetrieve**](PollApi.md#pollRetrieve) | **GET** /api/poll/{poll_id} | 
[**pollSessionRetrieve**](PollApi.md#pollSessionRetrieve) | **GET** /api/poll/session/{session_id} | 
[**pollSetAcceptingAnswerPartialUpdate**](PollApi.md#pollSetAcceptingAnswerPartialUpdate) | **PATCH** /api/poll/set-accepting-answer | 
[**pollSubmitResponseUpdate**](PollApi.md#pollSubmitResponseUpdate) | **PUT** /api/poll/submit-response | 

<a name="pollAnswerRetrieve"></a>
# **pollAnswerRetrieve**
> Answer pollAnswerRetrieve(poll_id)



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

let apiInstance = new PollPalApi.PollApi();
let poll_id = 56; // Number | 

apiInstance.pollAnswerRetrieve(poll_id).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **Number**|  | 

### Return type

[**Answer**](Answer.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="pollNextQuestionCreate"></a>
# **pollNextQuestionCreate**
> Poll pollNextQuestionCreate(body)



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

let apiInstance = new PollPalApi.PollApi();
let body = new PollPalApi.PollNextQuestion(); // PollNextQuestion | 

apiInstance.pollNextQuestionCreate(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PollNextQuestion**](PollNextQuestion.md)|  | 

### Return type

[**Poll**](Poll.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="pollResponsesList"></a>
# **pollResponsesList**
> [Response] pollResponsesList(poll_id)



Returns all responses for a poll with the provided poll_id.

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

let apiInstance = new PollPalApi.PollApi();
let poll_id = 56; // Number | 

apiInstance.pollResponsesList(poll_id).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **Number**|  | 

### Return type

[**[Response]**](Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="pollRetrieve"></a>
# **pollRetrieve**
> Poll pollRetrieve(poll_id)



Returns the poll with the provided poll_id.

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

let apiInstance = new PollPalApi.PollApi();
let poll_id = 56; // Number | 

apiInstance.pollRetrieve(poll_id).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **Number**|  | 

### Return type

[**Poll**](Poll.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="pollSessionRetrieve"></a>
# **pollSessionRetrieve**
> Poll pollSessionRetrieve(session_id)



Returns the poll from the session with the provided session_id.

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

let apiInstance = new PollPalApi.PollApi();
let session_id = 56; // Number | 

apiInstance.pollSessionRetrieve(session_id).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Number**|  | 

### Return type

[**Poll**](Poll.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="pollSetAcceptingAnswerPartialUpdate"></a>
# **pollSetAcceptingAnswerPartialUpdate**
> Poll pollSetAcceptingAnswerPartialUpdate(body)



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

let apiInstance = new PollPalApi.PollApi();
let body = new PollPalApi.PollSetAcceptingAnswers(); // PollSetAcceptingAnswers | 

apiInstance.pollSetAcceptingAnswerPartialUpdate(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PollSetAcceptingAnswers**](PollSetAcceptingAnswers.md)|  | 

### Return type

[**Poll**](Poll.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="pollSubmitResponseUpdate"></a>
# **pollSubmitResponseUpdate**
> Response pollSubmitResponseUpdate(body)



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

let apiInstance = new PollPalApi.PollApi();
let body = new PollPalApi.PollSubmitResponse(); // PollSubmitResponse | 

apiInstance.pollSubmitResponseUpdate(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PollSubmitResponse**](PollSubmitResponse.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

