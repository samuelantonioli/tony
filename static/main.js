(function() {
    // https://watson-speech.mybluemix.net/
    var btn = document.getElementById('recognize'),
        output = document.getElementById('output'),
        running = false,
        _stream;

    btn.onclick = function() {
        if (running) {
            if (_stream) {
                _stream.stop();
            }
            btn.classList.remove('active');
            running = false;
            return;
        }
        btn.classList.add('active');

        _stream = WatsonSpeech.SpeechToText.recognizeMicrophone({
            token: '{{token}}',
            continuous: false, // false = automatically stop transcription the first time a pause is detected
            outputElement: output // CSS selector or DOM Element
        });
        running = true;
        _stream.on('error', function(err) {
            console.log(err);
        });
        _stream.on('data', function(data) {
            output.style.color = '#777';
            running = true;
        });
        _stream.on('end', function() {
            running = false;
            btn.classList.remove('active');
            output.style.color = 'transparent';
            var cmd = output.innerHTML;
            if (!cmd) return;
            majax('/api/action', function() {
                // success
            }, function() {
                // error
            }, true, {
                command: cmd
            });
        });
    };
})();
