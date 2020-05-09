const data = {
    password: undefined,
    token: undefined,
    locked: false
};


class Locker {

    get status() {
        
        const status = data.locked;
        data.locked = false;

        return status;
    }

    lock(password) {

        if (this.validate_password(password)) {
            data.locked = true;
            return true;
        }
    }

    set_new_password(token, new_password) {

        if (!token || !new_password) {
            return false;
        } 

        if (!data.token || this.validate_token(token)) {

            data.token = token;
            data.password = new_password;

            return true;
        }
    }

    validate_password(password) {
        return (password === data.password);  
    }

    validate_token(token) {
        return (token === data.token);
    }
}


module.exports = Locker;