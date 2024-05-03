import ApiClient from "./Api/src/ApiClient";
import SessionApi from "./Api/src/api/SessionApi";
import QuestionApi from "./Api/src/api/QuestionApi";
import PollApi from "./Api/src/api/PollApi";

export default class PollPalApi {
  constructor() {
    this.apiClient = new ApiClient();
    this.apiClient.basePath = "http://localhost:8000";
    this.sessionApi = new SessionApi(this.apiClient);
    this.questionApi = new QuestionApi(this.apiClient);
    this.pollApi = new PollApi(this.apiClient);
  }
}
