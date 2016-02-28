
(cl:in-package :asdf)

(defsystem "sensor_server-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AddTwoInts" :depends-on ("_package_AddTwoInts"))
    (:file "_package_AddTwoInts" :depends-on ("_package"))
    (:file "GetSensVal" :depends-on ("_package_GetSensVal"))
    (:file "_package_GetSensVal" :depends-on ("_package"))
  ))