/**
 * Bybit API
 * ## REST API for the Bybit Exchange. Base URI: [https://api.bybit.com]  
 *
 * OpenAPI spec version: 0.2.10
 * Contact: support@bybit.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.math.BigDecimal;
import io.swagger.annotations.*;
import com.google.gson.annotations.SerializedName;

/**
 * Linear Order list Base
 **/
@ApiModel(description = "Linear Order list Base")
public class LinearOrderRecordsResponseBase {
  
  @SerializedName("ret_code")
  private BigDecimal retCode = null;
  @SerializedName("ret_msg")
  private String retMsg = null;
  @SerializedName("ext_code")
  private String extCode = null;
  @SerializedName("ext_info")
  private String extInfo = null;
  @SerializedName("result")
  private Object result = null;
  @SerializedName("time_now")
  private String timeNow = null;

  /**
   **/
  @ApiModelProperty(value = "")
  public BigDecimal getRetCode() {
    return retCode;
  }
  public void setRetCode(BigDecimal retCode) {
    this.retCode = retCode;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getRetMsg() {
    return retMsg;
  }
  public void setRetMsg(String retMsg) {
    this.retMsg = retMsg;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getExtCode() {
    return extCode;
  }
  public void setExtCode(String extCode) {
    this.extCode = extCode;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getExtInfo() {
    return extInfo;
  }
  public void setExtInfo(String extInfo) {
    this.extInfo = extInfo;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public Object getResult() {
    return result;
  }
  public void setResult(Object result) {
    this.result = result;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getTimeNow() {
    return timeNow;
  }
  public void setTimeNow(String timeNow) {
    this.timeNow = timeNow;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LinearOrderRecordsResponseBase linearOrderRecordsResponseBase = (LinearOrderRecordsResponseBase) o;
    return (this.retCode == null ? linearOrderRecordsResponseBase.retCode == null : this.retCode.equals(linearOrderRecordsResponseBase.retCode)) &&
        (this.retMsg == null ? linearOrderRecordsResponseBase.retMsg == null : this.retMsg.equals(linearOrderRecordsResponseBase.retMsg)) &&
        (this.extCode == null ? linearOrderRecordsResponseBase.extCode == null : this.extCode.equals(linearOrderRecordsResponseBase.extCode)) &&
        (this.extInfo == null ? linearOrderRecordsResponseBase.extInfo == null : this.extInfo.equals(linearOrderRecordsResponseBase.extInfo)) &&
        (this.result == null ? linearOrderRecordsResponseBase.result == null : this.result.equals(linearOrderRecordsResponseBase.result)) &&
        (this.timeNow == null ? linearOrderRecordsResponseBase.timeNow == null : this.timeNow.equals(linearOrderRecordsResponseBase.timeNow));
  }

  @Override
  public int hashCode() {
    int result = 17;
    result = 31 * result + (this.retCode == null ? 0: this.retCode.hashCode());
    result = 31 * result + (this.retMsg == null ? 0: this.retMsg.hashCode());
    result = 31 * result + (this.extCode == null ? 0: this.extCode.hashCode());
    result = 31 * result + (this.extInfo == null ? 0: this.extInfo.hashCode());
    result = 31 * result + (this.result == null ? 0: this.result.hashCode());
    result = 31 * result + (this.timeNow == null ? 0: this.timeNow.hashCode());
    return result;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class LinearOrderRecordsResponseBase {\n");
    
    sb.append("  retCode: ").append(retCode).append("\n");
    sb.append("  retMsg: ").append(retMsg).append("\n");
    sb.append("  extCode: ").append(extCode).append("\n");
    sb.append("  extInfo: ").append(extInfo).append("\n");
    sb.append("  result: ").append(result).append("\n");
    sb.append("  timeNow: ").append(timeNow).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}