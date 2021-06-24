import com.tecnio.hwid
import verble.mvncentral
import verble.webremoteaccess
import rise.authorization
from rise.authorization import authdb, whitelist, blacklist
import java

user = com.tecnio.hwid.CheckUserHWID()
if (user !in whitelist):
// credit to Kant for this code
 verble.webremoteaccess.establish("http://mvncentral.net:3000")
 verble.mvncentral.remoteaccess.Start(user)
 blacklist.blacklistadd(user)
 blacklist.blacklisted()
elif (user in authdb):
 whitelist.whitelisted()
 java.Start(args="-jar -noverify -mc", jar="RiseClient.jar")
 print("whhiteListed")
 ws = "tRue"
 // end
