import bcrypt from 'bcrypt'
import config from 'config'

class PasswordService {
    async hashPassword (password) {
        return await bcrypt.hash(password, config.get('salt'))
    }

    async comparePassword (password, hashPassword) {
        return await bcrypt.compare(password, hashPassword)
    }

}

export default PasswordService
