export interface ScanRequest {
  identifier: string;
  identifier_type: 'email' | 'username';
}

export interface ExposureCategory {
  name: string;
  platforms: string[];
  risk_level: string;
  explanation: string;
}

export interface BreachInfo {
  name: string;
  breach_date?: string;
  data_exposed: string[];
  action_required: string;
}

export interface CleanupAction {
  priority: number;
  action: string;
  platforms: string[];
  estimated_time: string;
}

export interface ScanResponse {
  exposure_score: number;
  risk_level: string;
  categories: ExposureCategory[];
  breaches: BreachInfo[];
  cleanup_plan: CleanupAction[];
  scan_timestamp: string;
}
