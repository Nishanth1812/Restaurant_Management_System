const API_BASE = "/api";

async function apiRequest(endpoint, method = "GET", body = null) {
  const token = localStorage.getItem("access_token");
  const headers = {
    "Content-Type": "application/json",
  };
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const config = {
    method,
    headers,
  };
  if (body) {
    config.body = JSON.stringify(body);
  }

  try {
    const response = await fetch(`${API_BASE}${endpoint}`, config);
    if (response.status === 401) {
      // Token expired or invalid
      logout();
      return null;
    }
    return response;
  } catch (error) {
    console.error("API Request failed", error);
    return null;
  }
}
