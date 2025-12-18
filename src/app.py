#!/usr/bin/env python3
"""
Vulnerable Python Application - FOR SECURITY TESTING ONLY
Contains intentional vulnerabilities for Semgrep detection
"""

import os
import subprocess
import sqlite3
import hashlib
import pickle
import yaml
from flask import Flask, request, render_template_string

app = Flask(__name__)

# VULNERABILITY: Hardcoded credentials (Semgrep + Gitleaks)
DATABASE_PASSWORD = "SuperSecret123!"
API_KEY = "sk-proj-abc123xyz789secretkey"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# VULNERABILITY: Hardcoded secret in connection string
DB_CONNECTION = "postgresql://admin:password123@localhost:5432/mydb"


@app.route('/search')
def search():
    # VULNERABILITY: SQL Injection
    user_input = request.args.get('query', '')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Bad: String concatenation in SQL query
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    cursor.execute(query)
    
    # Also bad: f-string SQL injection
    query2 = f"SELECT * FROM products WHERE id = {user_input}"
    cursor.execute(query2)
    
    return str(cursor.fetchall())


@app.route('/execute')
def execute_command():
    # VULNERABILITY: Command Injection
    cmd = request.args.get('cmd', 'ls')
    
    # Bad: Direct shell command execution with user input
    output = os.system(cmd)
    
    # Also bad: subprocess with shell=True
    result = subprocess.call(cmd, shell=True)
    
    # Also bad: subprocess.Popen with shell=True
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    
    return str(output)


@app.route('/render')
def render_page():
    # VULNERABILITY: Server-Side Template Injection (SSTI)
    template = request.args.get('template', 'Hello')
    return render_template_string(template)


@app.route('/hash')
def weak_hash():
    data = request.args.get('data', 'test')
    
    # VULNERABILITY: Weak cryptographic hash (MD5)
    md5_hash = hashlib.md5(data.encode()).hexdigest()
    
    # VULNERABILITY: Weak cryptographic hash (SHA1)
    sha1_hash = hashlib.sha1(data.encode()).hexdigest()
    
    return f"MD5: {md5_hash}, SHA1: {sha1_hash}"


@app.route('/deserialize')
def unsafe_deserialize():
    # VULNERABILITY: Unsafe deserialization
    data = request.args.get('data', '')
    
    # Bad: pickle.loads on untrusted data
    obj = pickle.loads(data.encode())
    
    return str(obj)


@app.route('/yaml')
def unsafe_yaml():
    # VULNERABILITY: Unsafe YAML loading
    yaml_data = request.args.get('data', '')
    
    # Bad: yaml.load without safe_load
    parsed = yaml.load(yaml_data)
    
    return str(parsed)


# VULNERABILITY: Binding to all interfaces
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
