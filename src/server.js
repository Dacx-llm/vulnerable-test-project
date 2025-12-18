/**
 * Vulnerable Node.js Application - FOR SECURITY TESTING ONLY
 * Contains intentional vulnerabilities for Semgrep detection
 */

const express = require('express');
const mysql = require('mysql');
const child_process = require('child_process');
const fs = require('fs');
const crypto = require('crypto');

const app = express();

// VULNERABILITY: Hardcoded credentials
const DB_PASSWORD = "admin123!";
const JWT_SECRET = "super-secret-jwt-key-12345";
const PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA2Z3qX2BTLS4e...\n-----END RSA PRIVATE KEY-----";

// VULNERABILITY: Hardcoded API keys
const STRIPE_API_KEY = "sk_live_abc123xyz789";
const SENDGRID_KEY = "SG.xxxx.yyyy";
const GITHUB_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";

// Database connection with hardcoded credentials
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'root123',  // VULNERABILITY: Hardcoded password
  database: 'myapp'
});

// VULNERABILITY: SQL Injection
app.get('/user', (req, res) => {
  const userId = req.query.id;
  const query = "SELECT * FROM users WHERE id = " + userId;
  connection.query(query, (err, results) => {
    res.json(results);
  });
});

// VULNERABILITY: Command Injection
app.get('/ping', (req, res) => {
  const host = req.query.host;
  child_process.exec('ping -c 1 ' + host, (err, stdout) => {
    res.send(stdout);
  });
});

// VULNERABILITY: Eval injection
app.get('/calc', (req, res) => {
  const expression = req.query.expr;
  const result = eval(expression);
  res.json({ result });
});

// VULNERABILITY: XSS (Cross-Site Scripting)
app.get('/greet', (req, res) => {
  const name = req.query.name;
  res.send(`<html><body><h1>Hello ${name}!</h1></body></html>`);
});

// VULNERABILITY: Path Traversal
app.get('/file', (req, res) => {
  const filename = req.query.name;
  const content = fs.readFileSync('/uploads/' + filename);
  res.send(content);
});

// VULNERABILITY: Weak cryptography
app.get('/encrypt', (req, res) => {
  const data = req.query.data;
  const hash = crypto.createHash('md5').update(data).digest('hex');
  res.json({ hash });
});

// VULNERABILITY: Insecure random
app.get('/token', (req, res) => {
  const token = Math.random().toString(36).substring(2);
  res.json({ token });
});

// VULNERABILITY: Binding to all interfaces
app.listen(3000, '0.0.0.0', () => {
  console.log('Server running on port 3000');
});
