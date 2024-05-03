import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import PollPalApi from "../PollPalApi";
import Paper from "@mui/material/Paper";
import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import PollSubmitResponse from "../Api/src/model/PollSubmitResponse";

const JoinSessionInput = ({ onSessionFound }) => {
  const [sessionId, setSessionId] = useState("");

  const handleJoinSession = async () => {
    const sessionApi = new PollPalApi().sessionApi;
    const session = await sessionApi.sessionGetRetrieve(sessionId);
    onSessionFound(session);
  };

  const handleInputChange = (event) => {
    const newValue = event.target.value;
    if (/^\d*$/.test(newValue)) {
      // Check if newValue is a number
      setSessionId(newValue);
    }
  };

  return (
    <Box display="flex" justifyContent="center" gap={3}>
      <TextField
        id="session-id"
        label="Session ID"
        variant="outlined"
        required
        value={sessionId}
        onChange={handleInputChange}
      />

      <Button variant="contained" onClick={handleJoinSession}>
        <Typography variant="button" fontWeight="bold">
          JOIN
        </Typography>
      </Button>
    </Box>
  );
};

const CreateSessionLink = () => (
  <Link to="/session/create" style={{ textDecoration: "none" }}>
    <Typography variant="body1" color="primary" sx={{ mt: 3 }}>
      Create a Session
    </Typography>
  </Link>
);

const InSession = ({ session }) => {
  const [poll, setPoll] = useState(undefined);
  const [answers, setAnswers] = useState([]);
  const [question, setQuestion] = useState(undefined);
  const [selectedAnswer, setSelectedAnswer] = useState("");
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    const pollApi = new PollPalApi().pollApi;
    const questionApi = new PollPalApi().questionApi;

    const fetchData = async () => {
      const pollResponse = await pollApi.pollSessionRetrieve(session.id);
      setPoll(pollResponse);

      const questionResponse = await questionApi.questionPollRetrieve(
        pollResponse.id,
      );
      setQuestion(questionResponse);

      const answersResponse = await questionApi.questionAnswerList(
        questionResponse.id,
      );
      setAnswers(answersResponse);
    };

    fetchData();
  }, [session]);

  const handleSubmit = async () => {
    setSubmitted(true);
    const pollApi = new PollPalApi().pollApi;
    await pollApi.pollSubmitResponseUpdate(
      new PollSubmitResponse(poll.id, answers[selectedAnswer].id),
    );
  };

  return (
    <Box
      display="flex"
      flexDirection="column"
      justifyContent="center"
      alignItems="center"
      sx={{ gap: 3, m: 3 }}
    >
      <Paper elevation={3}>
        <Typography variant="h3" component="div" sx={{ fontWeight: "bold" }}>
          Session ID:{session.id} "{session.label}"
        </Typography>

        <Typography
          variant="h4"
          component="div"
          sx={{ fontWeight: "bold", mt: 3 }}
        >
          Question: {question?.prompt}
        </Typography>

        {!submitted ? (
          <>
            <RadioGroup
              value={selectedAnswer}
              onChange={(e) => setSelectedAnswer(e.target.value)}
            >
              {answers.map((answer, index) => (
                <FormControlLabel
                  key={index}
                  value={index}
                  control={<Radio />}
                  label={answer.answer}
                />
              ))}
            </RadioGroup>

            <Button variant="contained" onClick={handleSubmit}>
              Submit Response
            </Button>
          </>
        ) : (
          <Typography variant="h5" component="div" sx={{ mt: 3 }}>
            Response Submitted
          </Typography>
        )}
      </Paper>
    </Box>
  );
};

const JoinSession = () => {
  const [sessionFound, setSessionFound] = useState(false);
  const [session, setSession] = useState(undefined);

  const handleSessionFound = (session) => {
    setSession(session);
    setSessionFound(true);
  };

  return (
    <>
      {!sessionFound && (
        <Box
          display="flex"
          flexDirection="column"
          justifyContent="center"
          alignItems="center"
          sx={{
            gap: 3,
            mt: 10,
          }}
        >
          <Typography variant="h1" component="div" sx={{ fontWeight: "bold" }}>
            PollPal
          </Typography>
          <Box
            display="flex"
            flexDirection="column"
            justifyContent="center"
            alignItems="center"
          >
            <JoinSessionInput onSessionFound={handleSessionFound} />
            <CreateSessionLink />
          </Box>
        </Box>
      )}

      {sessionFound && <InSession session={session} />}
    </>
  );
};

export default JoinSession;
