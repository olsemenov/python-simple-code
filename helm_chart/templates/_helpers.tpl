{{/*Image pull secrets are essentially a combination of registry, username, and password. You may need them in an application you are deploying, but to create them requires running base64 a couple of times
*/}}
{{- define "imagePullSecret" }}
{{- printf "{\"auths\": {\"%s\": {\"auth\": \"%s\"}}}" .Values.imageCredentials.registry (printf "%s:%s" .Values.imageCredentials.username .Values.imageCredentials.password | b64enc) | b64enc }}
{{- end }}