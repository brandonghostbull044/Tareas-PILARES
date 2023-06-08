const sing_up = document.querySelector('#sing-up');
const sing_up_form = document.querySelector('#sing-up-form');
const login = document.querySelector('#login');
const login_form = document.querySelector('#login-form');
login.addEventListener('click', toggleLogin)
sing_up.addEventListener('click', toggleSingUp);


function toggleLogin () {
    if (!sing_up_form.classList.contains('inactive')) {
        sing_up_form.classList.add('inactive');
    }

    login_form.classList.toggle('inactive');
}

function toggleSingUp () {
    if (!login_form.classList.contains('inactive')) {
        login_form.classList.add('inactive');
    }
    
    sing_up_form.classList.toggle('inactive');   
}
