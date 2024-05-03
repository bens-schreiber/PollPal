import React, { useState } from "react";
import PollPalApi from "../Api";
import Button from "@mui/material/Button";

export default function CreateSession() {
  const [sessionResult, setSessionResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const sessionApi = new PollPalApi().sessionApi;

  const handleButtonClick = async () => {
    if (isLoading) {
      return;
    }

    setIsLoading(true);
    sessionApi.sessionCreate({ label: "string" }, (error, data, response) => {
      if (error) {
        console.error(error);
      } else {
        console.log("API called successfully. Returned data: " + data);
        setSessionResult(data);
      }
      setIsLoading(false);
    });
  };

  return (
    <div>
      <Button
        variant="contained"
        color="primary"
        onClick={handleButtonClick}
        disabled={isLoading}
      >
        Create Session
      </Button>
      {sessionResult && (
        <div>Session Result: {JSON.stringify(sessionResult)}</div>
      )}
    </div>
  );
}
