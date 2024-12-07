This repository provides Python implementations for solving brute force challenges at three levels of difficulty:low, medium, and high.
Each level introduces different types of controls to simulate real-world scenarios where brute force techniques might encounter obstacles.

Levels Overview:
Low Level:
No security measures are implemented. The brute force script directly attempts all possible credential combinations without any interference.
Medium Level:
A 2-second delay is imposed by the system if incorrect credentials are provided. The script adapts by accounting for this delay to maintain efficiency.
High Level:
This level introduces two significant challenges:
A session token must be retrieved and included in each brute force attempt.
The delay for incorrect attempts is randomized between 0 and 3 seconds.
The script handles both obstacles by retrieving session tokens dynamically and managing randomized delays.

Disclaimer:
These scripts are for educational purposes only and are intended to demonstrate how different levels of security measures affect brute force techniques. Always use responsibly and only in environments where you have explicit permission to test.
