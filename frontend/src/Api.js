import ApiClient from "./Api/src/ApiClient";
import SessionApi from "./Api/src/api/SessionApi";

export default class PollPalApi {
  constructor() {
    this.apiClient = new ApiClient();
    this.apiClient.basePath = "http://localhost:8000";
    this.sessionApi = new SessionApi(this.apiClient);
  }
}
