const axios = require('axios'); // Make sure to import axios if you're using Node.js or have it available in your environment

axios.get('https://jsonplaceholder.typicode.com/todos')
    .then(response => {
        const data = response.data;
        let completedTasksCount = 0; // Initialize a variable outside the loop to count completed tasks
        data.forEach(obj => {
            if(obj.completed === true) {
                completedTasksCount++; // Increment the count for each completed task
            }
        });
        console.log(`Number of completed tasks: ${completedTasksCount}`);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
