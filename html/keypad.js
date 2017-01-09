// Get all the keys from document
var keys = document.querySelectorAll('#calculator span');
var pinDigits = 4;
var pinCode = '';


// Add onclick event to all the keys and perform operations
for(var i = 0; i < keys.length; i++) {
	keys[i].onclick = function(e) {
		// Get the input and button values
		var input = document.querySelector('.screen');
		var inputVal = input.innerHTML;
		var btnVal = this.innerHTML;
		
		// Append the key values (btnValue) to the pinCode string.
		// If Del key is pressed, delete last digit. 
		if(btnVal == 'Del') {
            pinCode = pinCode.substring(0, pinCode.length - 1);
		}
		
		else if (pinCode.length < pinDigits) {
            pinCode += btnVal;

		}

        /* Show the current pinCode. */
        input.innerHTML = "**********".substring(0, pinCode.length);

        /* If we hit the number of PIN code digits, submit the pin code. */
        if (pinCode.length == pinDigits) {
            document.getElementById('pin').value = pinCode;
            document.getElementById('openDoor').submit()
        }

		// prevent page jumps
		e.preventDefault();
	} 
}
