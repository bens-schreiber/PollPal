import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";

import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import JoinSession from "./Session/JoinSession";
import CreateSession from "./Session/CreateSession";

const darkTheme = createTheme({
  palette: {
    mode: "dark",
  },
});

const TopAppBar = () => (
  <AppBar position="static">
    <Toolbar>
      <IconButton
        size="large"
        edge="start"
        color="inherit"
        aria-label="menu"
        sx={{ mr: 2 }}
      ></IconButton>
      <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
        PollPal
      </Typography>
    </Toolbar>
  </AppBar>
);

export default function App() {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <TopAppBar />
      <Router>
        <Routes>
          <Route path="/" element={<JoinSession />} />
          <Route path="/session/join" element={<JoinSession />} />
          <Route path="/session/create" element={<CreateSession />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}
