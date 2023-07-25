const button1 = document.querySelector('.button1');

button1.addEventListener('mouseup', () => {
    alert('Button 1 pressed!');
    window.open('https://servertw.atlassian.net/jira/software/projects/WA/boards/11', '_blank');
})