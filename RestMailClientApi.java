public class RestClientApi { // test with python

	private String url = "http://localhost:8081/api/V1/mail";
	HttpClient httpclient = new DefaultHttpClient();
	private String session_token = null;
	// private String url = "http://dm1401024591792.fun25.co.kr/api/V2/";
	// private String url = "http://localhost:8080/aaa";
	// private String apiKey =
	// "6498a8ad1beb9d84d63035c5d1120c007fad6de706734db9689f8996707e0f7d";
	// private ObjectMapper objectMapper = new ObjectMapper();

	public RestClientApi() {
		// objectMapper.configure(SerializationFeature.INDENT_OUTPUT, true);
		// objectMapper.setDateFormat(df);
		DateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm");
	}

	private void test() {
		try {
			List<OV_MailApi> list = new LinkedList<OV_MailApi>();
			OV_MailApi item = new OV_MailApi();
			item.name = "hong";
			list.add(item);
			 
			for (int i = 0; i < 1; i++) {
				insert(list);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	/**
	 * 
	 * @param tasks
	 * @return
	 * @throws JsonGenerationException
	 * @throws JsonMappingException
	 * @throws IOException
	 */
	public int insert(List<OV_MailApi> tasks) throws JsonGenerationException, JsonMappingException, IOException {
		HttpPost request = new HttpPost(url);
		String jString = OV_Task.encodeList(tasks);
		StringEntity entity = new StringEntity(jString, "UTF-8");
		entity.setContentType("application/json; charset=utf-8");
		request.setEntity(entity);
		HttpResponse response = httpclient.execute(request);
		HttpEntity resEntity = response.getEntity();
		if (resEntity != null) {
			String s = getEntityString(entity);
			System.out.println("POST: " + s);
		}
		EntityUtils.consumeQuietly(response.getEntity());
		return 0;
	}

//	public void update(List<OV_Task> tasks) throws JsonGenerationException, JsonMappingException, IOException {
//		HttpPatch request = new HttpPatch(url);
//		String jString = OV_Task.encodeList(tasks);
//		{
//			StringEntity entity = new StringEntity(jString, "UTF-8");
//			entity.setContentType("application/json; charset=utf-8");
//			request.setEntity(entity);
//			HttpResponse response = httpclient.execute(request);
//			printResponse(response, null);
//		}
//
//	}

	public List<OV_Task> list() throws ClientProtocolException, IOException {
		System.out.println("FROM WEB");
		HttpGet request = new HttpGet(url + "/");
		// setApiKey(request);
		HttpResponse response = httpclient.execute(request);
		List<OV_Task> list = null;
		HttpEntity entity = response.getEntity();
		// System.out.println(response.getStatusLine());
		if (entity != null) {
			// System.out.println("--Response content length: " +
			// entity.getContentLength());
			String s = getEntityString(entity);
			// DebugConsole.println(s);
			list = OV_Task.decode(s);
			for (int i = 0; i < 30; i++) {
				// DebugConsole.println(list.get(i).dump());
			}
			// try {
			// ResourceUnit emp = objectMapper.readValue(s.getBytes(), ResourceUnit.class);
			// System.out.println("Response = " + emp);
			// } catch (IOException e1) {
			// // TODO Auto-generated catch block
			// e1.printStackTrace();
			// }
		}
		return list;
	}

	public void setApiKey77(HttpRequestBase request) {
		// request.addHeader("X-DreamFactory-Api-Key", apiKey);
		if (session_token != null) {
			request.addHeader("X-DreamFactory-Session-Token", session_token);
		}
	}

	public void login(String userId, String passwd) throws ClientProtocolException, IOException {
		HttpPost httpPost = new HttpPost(url + "user/session");
		// setApiKey(httpPost);
		ArrayList<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>();
		nameValuePairs.add(new BasicNameValuePair("app_name", "admin"));
		nameValuePairs.add(new BasicNameValuePair("email", "aainka@naver.com"));
		nameValuePairs.add(new BasicNameValuePair("password", "root123"));
		UrlEncodedFormEntity entity = new UrlEncodedFormEntity(nameValuePairs, "UTF-8");
		httpPost.setEntity(entity);
		HttpResponse response = httpclient.execute(httpPost);
		session_token = printResponse(response, "session_token");
	}

	public String printResponse(HttpResponse response, String findKey) {
		String findValue = null;
		HttpEntity entity = response.getEntity();
		// System.out.println(response.getStatusLine());
		if (entity != null) {
			// System.out.println("Response content length: " +
			// entity.getContentLength());
			String s = getEntityString(entity);
			try {
				if (findKey != null) {
					JSONParser parser = new JSONParser();
					JSONObject jsonObject = (JSONObject) parser.parse(s);
					findValue = jsonObject.get(findKey).toString();
				}
			} catch (ParseException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		return findValue;
	}

	private String getEntityString(HttpEntity entity) {
		String sContent = null;
		// System.out.println("Response content length: " +
		// entity.getContentLength());
		BufferedReader rd;
		try {
			rd = new BufferedReader(new InputStreamReader(entity.getContent(), "UTF-8"));
			String line = "";
			sContent = line;
			while ((line = rd.readLine()) != null) {
				// System.out.println(line);
				sContent += line;
			}
		} catch (UnsupportedOperationException | IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		// System.out.println("ans=" + sContent);
		return sContent;
	}

	public static void main(String arg[]) {
		new RestClientApi().test();
	}
}