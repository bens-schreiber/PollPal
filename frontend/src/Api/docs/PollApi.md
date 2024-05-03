# PollPalApi.PollApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pollAnswerRetrieve**](PollApi.md#pollAnswerRetrieve) | **GET** /api/poll/{poll_id}/answer | 
[**pollNextQuestionCreate**](PollApi.md#pollNextQuestionCreate) | **POST** /api/poll/next-question | 
[**pollSetAcceptingAnswerPartialUpdate**](PollApi.md#pollSetAcceptingAnswerPartialUpdate) | **PATCH** /api/poll/set-accepting-answer | 
[**pollSubmitResponseUpdate**](PollApi.md#pollSubmitResponseUpdate) | **PUT** /api/poll/submit-response | 

<a name="pollAnswerRetrieve"></a>
# **pollAnswerRetrieve**
> pollAnswerRetrieve(pollId)



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
let pollId = 56; // Number | 

apiInstance.pollAnswerRetrieve(pollId, (error, data, response) => {
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
 **pollId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="pollNextQuestionCreate"></a>
# **pollNextQuestionCreate**
> PollNextQuestion pollNextQuestionCreate(body)



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
let body = new PollPalApi.PollNextQuestionRequest(); // PollNextQuestionRequest | 

apiInstance.pollNextQuestionCreate(body, (error, data, response) => {
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
 **body** | [**PollNextQuestionRequest**](PollNextQuestionRequest.md)|  | 

### Return type

[**PollNextQuestion**](PollNextQuestion.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="pollSetAcceptingAnswerPartialUpdate"></a>
# **pollSetAcceptingAnswerPartialUpdate**
> PollSetAcceptingAnswers pollSetAcceptingAnswerPartialUpdate(opts)



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
let opts = { 
  'body': new PollPalApi.PatchedPollSetAcceptingAnswersRequest() // PatchedPollSetAcceptingAnswersRequest | 
};
apiInstance.pollSetAcceptingAnswerPartialUpdate(opts, (error, data, response) => {
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
 **body** | [**PatchedPollSetAcceptingAnswersRequest**](PatchedPollSetAcceptingAnswersRequest.md)|  | [optional] 

### Return type

[**PollSetAcceptingAnswers**](PollSetAcceptingAnswers.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="pollSubmitResponseUpdate"></a>
# **pollSubmitResponseUpdate**
> PollSubmitResponse pollSubmitResponseUpdate(body)



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
let body = new PollPalApi.PollSubmitResponseRequest(); // PollSubmitResponseRequest | 

apiInstance.pollSubmitResponseUpdate(body, (error, data, response) => {
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
 **body** | [**PollSubmitResponseRequest**](PollSubmitResponseRequest.md)|  | 

### Return type

[**PollSubmitResponse**](PollSubmitResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

