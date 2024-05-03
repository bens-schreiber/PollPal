import React, { useEffect, useState } from "react";
import PollPalApi from "../PollPalApi";
import {
  Button,
  TextField,
  Box,
  Paper,
  Checkbox,
  Typography,
} from "@mui/material";
import QuestionCreate from "../Api/src/model/QuestionCreate";
import QuestionCreateAnswerInput from "../Api/src/model/QuestionCreateAnswerInput";
import SessionStart from "../Api/src/model/SessionStart";
import PollNextQuestion from "../Api/src/model/PollNextQuestion";
import PollSetAcceptingAnswers from "../Api/src/model/PollSetAcceptingAnswers";

const FormPaper = ({ children }) => (
  <Paper elevation={3} sx={{ m: 3, p: 3 }}>
    {children}
  </Paper>
);

const FormBox = ({ children, onSubmit, flexDirection = "row" }) => (
  <Box
    component="form"
    onSubmit={onSubmit}
    display="flex"
    flexDirection={flexDirection}
    justifyContent="center"
    gap={3}
  >
    {children}
  </Box>
);

const CreateSessionForm = ({ onSessionCreated }) => {
  const [label, setLabel] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const sessionApi = new PollPalApi().sessionApi;

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (isLoading) {
      return;
    }

    setIsLoading(true);
    try {
      const session = await sessionApi.sessionCreate({
        label: label,
      });
      onSessionCreated(session);
    } catch {
      setIsLoading(false);
    }
  };

  return (
    <FormPaper>
      <FormBox onSubmit={handleSubmit}>
        <TextField
          label="Session Label"
          variant="outlined"
          value={label}
          onChange={(e) => setLabel(e.target.value)}
          required
        />
        <Button
          type="submit"
          variant="contained"
          color="primary"
          disabled={isLoading}
        >
          Create Session
        </Button>
      </FormBox>
    </FormPaper>
  );
};

const CreateQuestionsForm = ({ onQuestionsCreated }) => {
  const [questions, setQuestions] = useState([
    new QuestionCreate("", [new QuestionCreateAnswerInput("", false)]),
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const questionApi = new PollPalApi().questionApi;

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (isLoading) {
      return;
    }
    setIsLoading(true);
    var questionsList = [];
    try {
      for (let question of questions) {
        const questionResponse =
          await questionApi.questionCreateCreate(question);
        questionsList.push(questionResponse);
      }
      onQuestionsCreated(questionsList);
    } catch (e) {
      console.log(e);
      setIsLoading(false);
    }
  };

  const handleQuestionChange = (index, event) => {
    const newQuestions = [...questions];
    newQuestions[index] = new QuestionCreate(
      event.target.value,
      newQuestions[index].answers,
    );
    setQuestions(newQuestions);
  };

  const handleAnswerChange = (questionIndex, answerIndex, event) => {
    const newQuestions = [...questions];
    const newAnswer = new QuestionCreateAnswerInput(
      event.target.value,
      newQuestions[questionIndex].answers[answerIndex].is_correct,
    );
    newQuestions[questionIndex].answers[answerIndex] = newAnswer;
    setQuestions(newQuestions);
  };

  const handleToggleCorrect = (questionIndex, answerIndex) => {
    const newQuestions = [...questions];
    const newAnswer = new QuestionCreateAnswerInput(
      newQuestions[questionIndex].answers[answerIndex].answer,
      !newQuestions[questionIndex].answers[answerIndex].is_correct,
    );
    newQuestions[questionIndex].answers[answerIndex] = newAnswer;
    setQuestions(newQuestions);
  };

  const handleAddQuestion = () => {
    setQuestions([
      ...questions,
      new QuestionCreate("", [new QuestionCreateAnswerInput("", false)]),
    ]);
  };

  const handleAddAnswer = (index) => {
    const newQuestions = [...questions];
    newQuestions[index].answers.push(new QuestionCreateAnswerInput("", false));
    setQuestions(newQuestions);
  };

  return (
    <FormBox onSubmit={handleSubmit} flexDirection="column">
      <Box display="flex" flexDirection="column" flexWrap="wrap" gap={3}>
        {questions.map((question, questionIndex) => (
          <QuestionForm
            question={question}
            questionIndex={questionIndex}
            handleQuestionChange={(event) =>
              handleQuestionChange(questionIndex, event)
            }
            handleAddAnswer={() => handleAddAnswer(questionIndex)}
            handleAnswerChange={handleAnswerChange}
            handleToggleCorrect={handleToggleCorrect}
          />
        ))}
      </Box>
      <Button onClick={handleAddQuestion}>Add Question</Button>
      <Button
        type="submit"
        variant="contained"
        color="primary"
        disabled={isLoading}
      >
        Create Questions
      </Button>
    </FormBox>
  );
};

const QuestionForm = ({
  question,
  questionIndex,
  handleQuestionChange,
  handleAddAnswer,
  handleAnswerChange,
  handleToggleCorrect,
}) => {
  return (
    <FormPaper>
      <Box display="flex" flexDirection="column" gap={3}>
        <Typography variant="h5" component="h2">
          Question {questionIndex + 1}
        </Typography>
        <Box display="flex" gap={3}>
          <TextField
            label="Prompt"
            variant="outlined"
            value={question.prompt}
            onChange={handleQuestionChange}
            required
          />
          <Button onClick={handleAddAnswer}>Add Answer</Button>
        </Box>
        <Box display="flex" flexDirection="column" gap={3}>
          {question.answers.map((answer, answerIndex) => (
            <AnswerForm
              answer={answer}
              handleAnswerChange={(event) =>
                handleAnswerChange(questionIndex, answerIndex, event)
              }
              handleToggleCorrect={() =>
                handleToggleCorrect(questionIndex, answerIndex)
              }
            />
          ))}
        </Box>
      </Box>
    </FormPaper>
  );
};

const AnswerForm = ({ answer, handleAnswerChange, handleToggleCorrect }) => {
  return (
    <Box display="flex" flexDirection="row" gap={3}>
      <TextField
        label="Answer"
        variant="outlined"
        value={answer.answer}
        onChange={handleAnswerChange}
        required
      />
      <div>
        <Checkbox checked={answer.isCorrect} onChange={handleToggleCorrect} />
        <label>Correct</label>
      </div>
    </Box>
  );
};

const DisplayingQuestion = ({ question }) => {
  const [answers, setAnswers] = useState([]);

  useEffect(() => {
    const questionApi = new PollPalApi().questionApi;
    const fetchAnswers = async () => {
      const response = await questionApi.questionAnswerList(question.id);
      setAnswers(response);
    };

    fetchAnswers();
  }, [question]);

  return (
    <Box display="flex" flexDirection="column" gap={3}>
      <Typography variant="h5" component="h2">
        Displaying Question: {question.prompt}
      </Typography>

      {answers.map((answer, index) => (
        <Typography key={index}>
          Answer {index + 1}: {answer.answer}{" "}
          {answer.is_correct ? "(Correct)" : "(Incorrect)"}
        </Typography>
      ))}
    </Box>
  );
};

const NextQuestionButton = ({
  questionIndex,
  setQuestionIndex,
  poll,
  questions,
  setIsLoading,
}) => {
  const pollApi = new PollPalApi().pollApi;

  const handleNextQuestion = async () => {
    setIsLoading(true);
    try {
      await pollApi.pollNextQuestionCreate(
        new PollNextQuestion(poll.id, questions[questionIndex + 1].id),
      );
      setQuestionIndex(questionIndex + 1);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Button variant="contained" color="primary" onClick={handleNextQuestion}>
      Next Question
    </Button>
  );
};

const StopAcceptingAnswersButton = ({ poll, setIsLoading }) => {
  const pollApi = new PollPalApi().pollApi;

  const handleStopAcceptingAnswers = async () => {
    setIsLoading(true);
    try {
      await pollApi.pollSetAcceptingAnswerPartialUpdate(
        new PollSetAcceptingAnswers(poll.id, false),
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Button
      variant="contained"
      color="primary"
      onClick={handleStopAcceptingAnswers}
    >
      Stop Accepting Answers
    </Button>
  );
};

const StartPollForm = ({ session, questions }) => {
  const sessionApi = new PollPalApi().sessionApi;
  const [poll, setPoll] = useState(undefined);
  const [pollStarted, setPollStarted] = useState(false);
  const [questionIndex, setQuestionIndex] = useState(0);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event) => {
    const response = await sessionApi.sessionStartCreate(
      new SessionStart(session.id, questions[questionIndex].id),
    );
    setPoll(response);
    setPollStarted(true);
  };

  return (
    <FormPaper>
      {!isLoading && (
        <FormBox>
          {!pollStarted && (
            <Button variant="contained" color="primary" onClick={handleSubmit}>
              Start Poll
            </Button>
          )}

          {pollStarted && (
            <DisplayingQuestion question={questions[questionIndex]} />
          )}

          {pollStarted && questionIndex < questions.length - 1 && (
            <NextQuestionButton
              questionIndex={questionIndex}
              setQuestionIndex={setQuestionIndex}
              poll={poll}
              questions={questions}
              setIsLoading={setIsLoading}
            />
          )}

          {pollStarted && (
            <StopAcceptingAnswersButton
              poll={poll}
              setIsLoading={setIsLoading}
            />
          )}
        </FormBox>
      )}
      {pollStarted && <>Session Code: {session.id}</>}

      {pollStarted && <FindResponses poll={poll} />}
    </FormPaper>
  );
};

const FindResponses = ({ poll }) => {
  const [responses, setResponses] = useState([]);

  useEffect(() => {
    const interval = setInterval(async () => {
      const pollApi = new PollPalApi().pollApi;
      try {
        const response = await pollApi.pollResponsesList(poll.id);
        setResponses(response);
      } catch {}
    }, 2000);

    return () => clearInterval(interval);
  }, [poll]);

  return (
    <Box display="flex" flexDirection="column" gap={3}>
      <Typography variant="h5" component="h2">
        Responses
      </Typography>
      {responses.map((response, index) => (
        <Typography key={index}>
          Response {index + 1}: {response.id}
        </Typography>
      ))}
    </Box>
  );
};

const CreateSession = () => {
  const [sessionCreated, setSessionCreated] = useState(false);
  const [session, setSession] = useState();
  const [questionsCreated, setQuestionsCreated] = useState(false);
  const [questions, setQuestions] = useState();

  const handleSessionCreated = (session) => {
    setSessionCreated(true);
    setSession(session);
  };

  const handleQuestionsCreated = (questions) => {
    setQuestionsCreated(true);
    console.log(questions);
    setQuestions(questions);
  };

  return (
    <>
      {sessionCreated && !questionsCreated ? (
        <CreateQuestionsForm onQuestionsCreated={handleQuestionsCreated} />
      ) : null}

      {questionsCreated ? (
        <StartPollForm questions={questions} session={session} />
      ) : null}

      {!sessionCreated && !questionsCreated ? (
        <CreateSessionForm onSessionCreated={handleSessionCreated} />
      ) : null}
    </>
  );
};

export default CreateSession;
