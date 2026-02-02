import { useState } from 'react';
import { apiClient } from '../lib/apiClient';
import type { ScanRequest, ScanResponse } from '../types/api.types';

export const useScan = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<ScanResponse | null>(null);

  const scan = async (request: ScanRequest) => {
    setLoading(true);
    setError(null);
    
    try {
      const result = await apiClient.scan(request);
      setData(result);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Scan failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setData(null);
    setError(null);
  };

  return { scan, loading, error, data, reset };
};
