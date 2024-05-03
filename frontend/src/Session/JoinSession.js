import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { Link } from "react-router-dom";

function JoinSessionInput() {
  return (
    <Box display="flex" justifyContent="center" gap={3}>
      <TextField id="session-id" label="Session ID" variant="outlined" />

      <Button variant="contained">
        <Typography variant="button" fontWeight="bold">
          JOIN
        </Typography>
      </Button>
    </Box>
  );
}

function CreateSessionLink() {
  return (
    <Link to="/session/create" style={{ textDecoration: "none" }}>
      <Typography variant="body1" color="primary" sx={{ mt: 3 }}>
        Create a Session
      </Typography>
    </Link>
  );
}

function SessionField() {
  return (
    <Box
      display="flex"
      flexDirection="column"
      justifyContent="center"
      alignItems="center"
    >
      <JoinSessionInput />
      <CreateSessionLink />
    </Box>
  );
}

export default function JoinSession() {
  return (
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

      <SessionField />
    </Box>
  );
}
