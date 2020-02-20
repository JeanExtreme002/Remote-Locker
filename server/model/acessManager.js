manager = {

    accessToken: undefined,
    password: undefined,

    setPassword: function(accessToken, newPassword){

        if (!accessToken || !newPassword){
            return false;

        }else if (!this.accessToken || this.accessToken === accessToken){

            this.accessToken = accessToken;
            this.password = newPassword;
            return true;
        }
    },

    validatePassword: function(password){

        if (password === this.password){
            return true;
            
        }else{
            return false;
        }
    },

    validateToken: function(token){

        if (token === this.accessToken){
            return true;

        }else{
            return false;
        }
    },

}

module.exports = manager;