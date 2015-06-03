$(document).ready(

	function(){

		
		$('#create-table-button').click(function(){
			var secretKey=prompt("Enter the secret key for this sheet");
			$('.read-value').each(function(){
				var l = $(this).val().toString();
				if(l != ""){
				var encrypted=CryptoJS.DES.encrypt(l, secretKey);
				var encryptedMessage = encrypted.toString();
				$(this).val(encryptedMessage);
				console.log($(this).val());
				}
				
			});
			document.getElementById("create-table-form").submit();
			
			
		});


		$('#create-group-button').click(function(){
			documnet.getElementById("create-group-form").submit();

		});
		

		$('#create-group-table-button').click(function(){
			var secretKey=prompt("Enter the secret key for this sheet");
			$('.read-value').each(function(){
				var l = $(this).val().toString();
				if(l != ""){
				var encrypted=CryptoJS.DES.encrypt(l, secretKey);
				var encryptedMessage = encrypted.toString();
				$(this).val(encryptedMessage);
				console.log($(this).val());
				}
				
			});
			document.getElementById("create-table-form").submit();

		});

		$('#add-member-button').click(function(){
			document.getElementById("add-new-member").submit();
		});


		


});




