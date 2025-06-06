import { handleRoute } from '@/app/utils/api_utils';
import { NextRequest, NextResponse } from "next/server";

export async function POST(request: NextRequest) {
  const endpoint = "/job.JobInterface/GetJob";
  const method = request.method;
  if (method !== 'POST') {
    return NextResponse.json({ error: 'Invalid method. Only POST is allowed.' }, { status: 405 });
  }

  const body = JSON.stringify(await request.json());
  const jsonBody = JSON.parse(body);
  if (!jsonBody || typeof jsonBody !== 'object') {
    return NextResponse.json({ error: 'Invalid request body' }, { status: 400 });
  }

  const response = await handleRoute(method, endpoint, body);
  const responseData = await response.json();
  
  if (!response.ok) return NextResponse.json({ error: responseData.error, status: response.status});
  return NextResponse.json({ data: responseData.data.job, status: responseData.status});
}
