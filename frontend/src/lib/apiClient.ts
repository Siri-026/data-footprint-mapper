import axios from 'axios';
import type { ScanRequest, ScanResponse } from '../types/api.types';

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const apiClient = {
  scan: async (data: ScanRequest): Promise<ScanResponse> => {
    const response = await axios.post(`${API_BASE}/api/scan`, data);
    return response.data;
  },
  
  health: async () => {
    const response = await axios.get(`${API_BASE}/api/health`);
    return response.data;
  }
};
