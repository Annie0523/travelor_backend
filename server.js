const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 8887; // Backend port

// Middleware
app.use(cors()); // Enable CORS for frontend communication
app.use(bodyParser.json()); // Parse JSON request bodies

// Simulated database (in-memory)
let comments = []; // Store comments in memory (resets on server restart)

// API to get all comments
app.get('/comments', (req, res) => {
    res.json(comments); // Respond with all comments
});

// API to post a new comment
app.post('/comments', (req, res) => {
    const { comment } = req.body; // Extract the comment from request body
    if (!comment) {
        return res.status(400).json({ error: 'Comment is required' }); // Handle missing comment
    }
    const newComment = { id: comments.length + 1, comment }; // Create a new comment with an ID
    comments.push(newComment); // Add it to the in-memory database
    res.status(201).json(newComment); // Respond with the newly added comment
});

// Start the server
app.listen(port, () => {
    console.log(`Backend server is running on http://localhost:${port}`);
});
