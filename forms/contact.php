<?php
    use PHPMailer\PHPMailer\PHPMailer;
    use PHPMailer\PHPMailer\Exception;

    require 'src/Exception.php'; 
    require 'src/PHPMailer.php';
    require 'src/SMTP.php';

    // Verifica si se han enviado datos por POST
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        
        if (isset($_POST["nombre"]) && isset($_POST["correo"]) && isset($_POST["asunto"])&& isset($_POST["mensaje"])){
            $from_name = $_POST['nombre'];
            $from_mail = $_POST['correo'];
            $from_asunt = $_POST['asunto'];
            $from_message = $_POST['mensaje'];
            $mail = new PHPMailer(true);
            //Server settings
            $mail->SMTPDebug = 0;                      //Enable verbose debug output
            $mail->isSMTP();                                            //Send using SMTP
            $mail->Host       = 'smtp.gmail.com';                     //Set the SMTP server to send through
            $mail->SMTPAuth   = true;                                   //Enable SMTP authentication
            $mail->Username   = 'dtecnologia99@gmail.com';                     //SMTP username
            $mail->Password   = 'dmevqiuegtguhfgu';                               //SMTP password
            $mail->SMTPSecure = 'tls';            //Enable implicit TLS encryption
            $mail->Port       = 587;                                    //TCP port to connect to; use 587 if you have set `SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS`
        
            //Recipients
            $mail->setFrom('dtecnologia99@gmail.com', 'Aseguramos');
            $mail->addAddress('tecnologia48hd3@gmail.com');     //Add a recipient
        
            //Attachments
            // $mail->addAttachment('/var/tmp/file.tar.gz');         //Add attachments
            // $mail->addAttachment('/tmp/image.jpg', 'new.jpg');    //Optional name
        
            //Content
            $mail->isHTML(true);                                  //Set email format to HTML
            $mail->Subject = "Ecosistema - Contactanos";
            $mail->Body = "
                Nombre Completo: $from_name $from_mail <br>
                Asunto: $from_asunt<br>
                Mensaje: $from_message <br>";
            $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';
            $mail->send();
            
            //devuelve una respuesta 
            $response = array(
                "success" => true,
                "message" => "¡El formulario se envió correctamente!"
            );
        } else {
            // Si falta algún campo, devuelve un mensaje de error
            $response = array(
                "success" => false,
                "message" => "Faltan datos en el formulario"
            );
        }
    } else {
        // Si no se ha recibido una solicitud POST, devuelve un mensaje de error
        $response = array(
            "success" => false,
            "message" => "Acceso no válido"
        );
    }

    // Devuelve la respuesta como JSON
    echo json_encode($response, JSON_UNESCAPED_UNICODE);

?>