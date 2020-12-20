// Get modal element

// Get modal element

var modal = document.getElementById('simpleModal');


//get close modal button

var closeBtn = document.getElementsByClassName('closeBtn')[0];




//Listen for close click
closeBtn.addEventListener('click',closeModal)

//Function to open modal
function openModal()
{
    modal.style.display = 'block';
}


function closeModal(){
    modal.style.display = 'none';  
}