document.addEventListener('DOMContentLoaded', function() {
    var messageTextArea = document.getElementById('user-input');
  
    messageTextArea.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            var form = messageTextArea.closest('form');
            form.submit();
        } 
    });
  });  

window.addEventListener('load', function() {
    var messageContainer = document.getElementById('chat-container');
    messageContainer.scrollTop = messageContainer.scrollHeight;
});

