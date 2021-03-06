/*
 * Bybit API
 *
 * ## REST API for the Bybit Exchange. Base URI: [https://api.bybit.com]  
 *
 * API version: 0.2.10
 * Contact: support@bybit.com
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package swagger

type LinearRiskLimitResp struct {
	CreatedAt string `json:"created_at,omitempty"`
	Id int32 `json:"id,omitempty"`
	IsLowestRisk int32 `json:"is_lowest_risk,omitempty"`
	Limit int64 `json:"limit,omitempty"`
	MaintainMargin float64 `json:"maintain_margin,omitempty"`
	Section []string `json:"section,omitempty"`
	StartingMargin float64 `json:"starting_margin,omitempty"`
	Symbol string `json:"symbol,omitempty"`
	UpdatedAt string `json:"updated_at,omitempty"`
}
