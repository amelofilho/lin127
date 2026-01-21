#!/usr/bin/env python3
"""
Student return script to receive feedback on
Usage: python return.py <assignment_id>
"""

import sys
import os
import requests
import json

# Configuration
SERVER_URL = "https://robvoigt.net/lin127/return/"
if not os.path.exists('identity.txt'):
    print(f"Error: Identity file not found in 'identity.txt'")
    print("Please create this file as described in A1.")
    sys.exit(1)

try:
    NAME, EMAIL, SECRET_WORD = open('identity.txt').read().strip().split(',')
except:
    print(f"Error: Identity file couldn't be loaded properly.")
    print("Please create this file as described in A1.")
    sys.exit(1)

def return_assignment(assignment_id):
    """
    Return assignment from server. 
    """
    
    main_files = {'a1': 'a1.txt',
                 'a2': 'a2.sh',
                 'a3': 'a3.py',
                 'a4': 'a4.py',
                 'a5': 'a5.ipynb',
                 'a6': 'a6.ipynb'}

    if not assignment_id in main_files:
        print(f"Error: Assignment ID must be one of a1, a2, a3, a4, a5, or a6. You entered {assignment_id} - try again.")
        return False
    
    # Prepare form data
    data = {
        'assignment': assignment_id.strip(),
        'student': EMAIL.strip(),
        'secret_word': SECRET_WORD.strip()
    }

    
    print(f"Returning {assignment_id}...")

    try:
        response = requests.post(
            SERVER_URL + assignment_id,
            data=data,
            timeout=30
        )        
        if response.status_code == 200:
            filename = response.headers.get('X-Filename')
            with open(f"{assignment_id}/{filename}", 'wb') as f:
                f.write(response.content)
            print(f"\n✓ Feedback returned successfully.")
            print(f"  Assignment: {assignment_id}")
            print(f"Check your assignment directory for {filename}")

            return True
        else:            
            error = response.json().get('error', 'Unknown error')
            print(f"\n✗ Submission failed: {error}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"\n✗ Connection error: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python return.py <assignment_id>")
        print("\nExample:")
        print("  python return.py a1")
        sys.exit(1)
    
    assignment_id = sys.argv[1].strip('/').lower()
    
    success = return_assignment(assignment_id)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
