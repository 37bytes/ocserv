DEFAULT_USER = "nobody"

import syslog
import urllib3
import sys

def auth_log(msg):
    """ Save to log /var/log/auth.log """
    syslog.openlog(facility=syslog.LOG_AUTH)
    syslog.syslog("Authentication with python: " + str(msg))
    syslog.closelog()


auth_log(sys.version)
auth_log(sys.path)

def pam_sm_authenticate(pamh, flags, argv):
  try:
    user = pamh.get_user(None)
  except pamh.exception as e:
    return pamh.PAM_AUTH_ERR
    #return e.pam_result

  try:

    if user == None:
      pam.user = DEFAULT_USER
    http = urllib3.PoolManager()
    req = http.request('POST','https://bot.37b.io/communicate/?username=' + user)

#    auth_log("    Got response")

    code = req.data[1:-1].decode()

#    auth_log("    Got bot code: {} ".format(code))

    resp = pamh.conversation(pamh.Message(2, 'Auth code'))

#  auth_log("    Got response code: {} ".format(resp.resp))

    c = "{}".format(code)
    r = "{}".format(resp.resp)

#  auth_log("    R: {}, C: {} ".format(r,c))

    if (r == c):
#    auth_log("   Auth OK")
      return pamh.PAM_SUCCESS
    else:
#    auth_log("   Auth FAIL")
      return pamh.PAM_AUTH_ERR
  except:
    return pamh.PAM_AUTH_ERR


def pam_sm_setcred(pamh, flags, argv):
  auth_log("pam_sm_setcred")
  return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt(pamh, flags, argv):
  auth_log("acct_mgmt")
  return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
  auth_log("open_session")
  return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
  auth_log("close_session")
  return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
  auth_log("chauthtok")
  return pamh.PAM_SUCCESS

