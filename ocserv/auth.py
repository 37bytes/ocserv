DEFAULT_USER = "nobody"

import syslog
import urllib2

def auth_log(msg):
    """ Save to log /var/log/auth.log """
    syslog.openlog(facility=syslog.LOG_AUTH)
    syslog.syslog("Authentication with python: " + str(msg))
    syslog.closelog()

def pam_sm_authenticate(pamh, flags, argv):
  try:
    user = pamh.get_user(None)
  except pamh.exception as e:
    return e.pam_result
  if user == None:
    pam.user = DEFAULT_USER
  response = urllib2.urlopen(urllib2.Request('OTP_URL' + user, {}))
  code = response.read()[1:-1]
  auth_log(user)
  resp = pamh.conversation(pamh.Message(2, 'Auth code'))
  if (str(resp.resp) == code):
    return pamh.PAM_SUCCESS
  else:
    return pamh.PAM_AUTH_ERR

def pam_sm_setcred(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
  return pamh.PAM_SUCCESS