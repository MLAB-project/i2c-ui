; Auto-generated. Do not edit!


(cl:in-package sensor_server-srv)


;//! \htmlinclude GetSensVal-request.msg.html

(cl:defclass <GetSensVal-request> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (data
    :reader data
    :initarg :data
    :type cl:string
    :initform ""))
)

(cl:defclass GetSensVal-request (<GetSensVal-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetSensVal-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetSensVal-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor_server-srv:<GetSensVal-request> is deprecated: use sensor_server-srv:GetSensVal-request instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <GetSensVal-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor_server-srv:name-val is deprecated.  Use sensor_server-srv:name instead.")
  (name m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <GetSensVal-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor_server-srv:data-val is deprecated.  Use sensor_server-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetSensVal-request>) ostream)
  "Serializes a message object of type '<GetSensVal-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetSensVal-request>) istream)
  "Deserializes a message object of type '<GetSensVal-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'data) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'data) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetSensVal-request>)))
  "Returns string type for a service object of type '<GetSensVal-request>"
  "sensor_server/GetSensValRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetSensVal-request)))
  "Returns string type for a service object of type 'GetSensVal-request"
  "sensor_server/GetSensValRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetSensVal-request>)))
  "Returns md5sum for a message object of type '<GetSensVal-request>"
  "1bc3537bb8034a7562e9cc5973528637")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetSensVal-request)))
  "Returns md5sum for a message object of type 'GetSensVal-request"
  "1bc3537bb8034a7562e9cc5973528637")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetSensVal-request>)))
  "Returns full string definition for message of type '<GetSensVal-request>"
  (cl:format cl:nil "string name~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetSensVal-request)))
  "Returns full string definition for message of type 'GetSensVal-request"
  (cl:format cl:nil "string name~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetSensVal-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4 (cl:length (cl:slot-value msg 'data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetSensVal-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GetSensVal-request
    (cl:cons ':name (name msg))
    (cl:cons ':data (data msg))
))
;//! \htmlinclude GetSensVal-response.msg.html

(cl:defclass <GetSensVal-response> (roslisp-msg-protocol:ros-message)
  ((val
    :reader val
    :initarg :val
    :type cl:integer
    :initform 0))
)

(cl:defclass GetSensVal-response (<GetSensVal-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetSensVal-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetSensVal-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor_server-srv:<GetSensVal-response> is deprecated: use sensor_server-srv:GetSensVal-response instead.")))

(cl:ensure-generic-function 'val-val :lambda-list '(m))
(cl:defmethod val-val ((m <GetSensVal-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor_server-srv:val-val is deprecated.  Use sensor_server-srv:val instead.")
  (val m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetSensVal-response>) ostream)
  "Serializes a message object of type '<GetSensVal-response>"
  (cl:let* ((signed (cl:slot-value msg 'val)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetSensVal-response>) istream)
  "Deserializes a message object of type '<GetSensVal-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'val) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetSensVal-response>)))
  "Returns string type for a service object of type '<GetSensVal-response>"
  "sensor_server/GetSensValResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetSensVal-response)))
  "Returns string type for a service object of type 'GetSensVal-response"
  "sensor_server/GetSensValResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetSensVal-response>)))
  "Returns md5sum for a message object of type '<GetSensVal-response>"
  "1bc3537bb8034a7562e9cc5973528637")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetSensVal-response)))
  "Returns md5sum for a message object of type 'GetSensVal-response"
  "1bc3537bb8034a7562e9cc5973528637")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetSensVal-response>)))
  "Returns full string definition for message of type '<GetSensVal-response>"
  (cl:format cl:nil "int64 val~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetSensVal-response)))
  "Returns full string definition for message of type 'GetSensVal-response"
  (cl:format cl:nil "int64 val~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetSensVal-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetSensVal-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GetSensVal-response
    (cl:cons ':val (val msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GetSensVal)))
  'GetSensVal-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GetSensVal)))
  'GetSensVal-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetSensVal)))
  "Returns string type for a service object of type '<GetSensVal>"
  "sensor_server/GetSensVal")